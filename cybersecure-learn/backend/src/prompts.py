def build_prompt(user_code: str, vulnerability_context: str) -> str:
    """
    Builds a prompt for the GPT-4 model by injecting user code and vulnerability context.

    Args:
        user_code (str): The code submitted by the user.
        vulnerability_context (str): Context about potential vulnerabilities.

    Returns:
        str: The formatted prompt for the GPT-4 model.
    """
    prompt = (
        "You are a secure coding tutor. Analyze the following code for vulnerabilities:\n\n"
        f"User Code:\n{user_code}\n\n"
        f"Vulnerability Context:\n{vulnerability_context}\n\n"
        "Please provide a detailed analysis, including any vulnerabilities found, "
        "explanations, and suggestions for secure alternatives."
    )
    return prompt


def build_vulnerability_explanation(vulnerability_name: str) -> str:
    """
    Builds a prompt for explaining a specific vulnerability.

    Args:
        vulnerability_name (str): The name of the vulnerability to explain.

    Returns:
        str: The formatted explanation prompt for the GPT-4 model.
    """
    explanation_prompt = (
        f"Explain the {vulnerability_name} vulnerability, including its risks, "
        "how it can be exploited, and best practices for mitigation."
    )
    return explanation_prompt