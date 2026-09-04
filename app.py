import os
import tempfile
from io import StringIO

import streamlit as st
import ollama
from pylint.lint import Run
from pylint.reporters.text import TextReporter


# ---------------------------------------------------------
# Streamlit Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="💻",
    layout="wide"
)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.header("💻 About Me")

    st.write(
        "Humaam Hussain/ Software Engineer / "
        " AIML Enthusiast"
    )

    st.markdown(
        "[GitHub](https://github.com/HUMAAM20)"
    )

    st.markdown(
        "[LinkedIn](www.linkedin.com/in/humaam-hussain-792403286)"
    )

    st.divider()

    st.info(
        "This application combines Pylint static analysis "
        "with local AI-powered code review using Llama 3.2."
    )

    st.success(
        "🟢 AI runs locally with Ollama"
    )


# ---------------------------------------------------------
# Main Application
# ---------------------------------------------------------

st.title("🤖 AI-Powered Code Reviewer")

st.markdown(
    """
    Paste your Python code below and get a detailed review
    using **Pylint static analysis** and
    **Llama 3.2 local AI analysis**.
    """
)

st.header("📝 Submit Your Code")


code_input = st.text_area(
    "Enter Python code here",
    height=300,
    placeholder="""Example:

def hello():
    print("Hello, World!")
"""
)


submit_button = st.button(
    "🔍 Review Code",
    type="primary"
)


# ---------------------------------------------------------
# Review Process
# ---------------------------------------------------------

if submit_button:

    if not code_input.strip():

        st.warning(
            "Please enter some Python code first."
        )

    else:

        # -------------------------------------------------
        # Create temporary Python file
        # -------------------------------------------------

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as temp_file:

            temp_file.write(code_input)
            temp_file_path = temp_file.name


        # -------------------------------------------------
        # Initialize results
        # -------------------------------------------------

        pylint_results = ""
        ai_feedback = ""


        # -------------------------------------------------
        # Create Tabs
        # -------------------------------------------------

        tab1, tab2, tab3 = st.tabs(
            [
                "🔎 Static Analysis",
                "🤖 AI Feedback",
                "📥 Download Report"
            ]
        )


        # =================================================
        # TAB 1 - PYLINT
        # =================================================

        with tab1:

            st.subheader(
                "🔎 Static Analysis (Pylint)"
            )

            output = StringIO()

            reporter = TextReporter(output)

            try:

                Run(
                    [temp_file_path],
                    reporter=reporter,
                    exit=False
                )

                pylint_results = output.getvalue()

                if pylint_results:

                    st.code(
                        pylint_results,
                        language="text"
                    )

                else:

                    st.success(
                        "✅ No Pylint issues were detected."
                    )

            except Exception as e:

                pylint_results = (
                    f"Pylint error: {e}"
                )

                st.error(
                    pylint_results
                )


        # =================================================
        # TAB 2 - LOCAL AI REVIEW
        # =================================================

        with tab2:

            st.subheader(
                "🤖 Llama 3.2 AI Feedback"
            )

            prompt = f"""
You are an expert Python software engineer
and professional code reviewer.

Review the following Python code carefully.

Provide a detailed code review using these sections:

## 1. Code Quality Score

Give a score from 1 to 10 and explain the score.

## 2. Code Quality

Analyze:

- Readability
- Code structure
- Naming conventions
- Maintainability
- Organization

## 3. Bugs and Logical Issues

Identify:

- Bugs
- Runtime errors
- Logical problems
- Edge cases

## 4. Security Analysis

Identify potential security vulnerabilities
or unsafe programming practices.

## 5. Performance

Identify inefficient operations and suggest
possible optimizations.

## 6. Best Practices

Explain how the code can better follow
Python best practices.

## 7. Improved Code

Provide a cleaner and improved version
of the submitted code.

## 8. Explanation

Explain why the improved version is better.

Here is the Python code:

```python
{code_input}

"""

        try:

            with st.spinner(
                "🧠 Llama 3.2 is analyzing your code..."
            ):

                response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an expert Python "
                                "software engineer and "
                                "professional code reviewer."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

            ai_feedback = (
                response["message"]["content"]
            )

            st.markdown(
                ai_feedback
            )

        except Exception as e:

            ai_feedback = (
                f"Ollama error: {e}"
            )

            st.error(
                ai_feedback
            )

            st.info(
                """
                Make sure Ollama is installed and running.

                Test it in PowerShell with:

                ollama run llama3.2:1b
                """
            )


    # =================================================
    # TAB 3 - DOWNLOAD REPORT
    # =================================================

    with tab3:

        st.subheader(
            "📥 Download Review Report"
        )

        report = f"""# AI Code Review Report"""