"""Tests for scripts/validate_papers.py clean_latex_artifacts.

Covers the artifact classes the validator itself flags via LATEX_PATTERNS
(math delimiters, citation commands, command wrappers incl. nested
underline-href chains, LaTeX quotes, and caret superscripts like R^2).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

from validate_papers import clean_latex_artifacts


def test_inline_math():
    assert clean_latex_artifacts("gain of $x=2$ units") == "gain of x=2 units"
    assert clean_latex_artifacts(r"y \(>\) z") == "y > z"


def test_citation_command_removed():
    s = "Building on the framework \\citep{mankiw2020}, we derive a bound."
    assert clean_latex_artifacts(s) == "Building on the framework, we derive a bound."
    s2 = "Prior work \\citet{smith2020} shows growth."
    assert clean_latex_artifacts(s2) == "Prior work shows growth."


def test_generic_command_wrappers():
    assert clean_latex_artifacts(r"we propose \texttt{MenuNet}") == "we propose MenuNet"
    assert clean_latex_artifacts(r"introduce \textsc{MOCA-Agent} now") == "introduce MOCA-Agent now"
    assert clean_latex_artifacts(r"the \textit{same} holds") == "the same holds"


def test_nested_command_with_href():
    s = r"code at \underline{\href{https://github.com/X}{https://github.com/X}} online"
    assert clean_latex_artifacts(s) == "code at https://github.com/X online"


def test_mbox_with_latex_quotes():
    s = r"described as a \mbox{``power couple,''} based on growth"
    assert clean_latex_artifacts(s) == 'described as a "power couple," based on growth'


def test_caret_superscript():
    assert clean_latex_artifacts("fit (R^2 = 0.983) here") == "fit (R\u00b2 = 0.983) here"
    assert clean_latex_artifacts("(R^2=0.44)") == "(R\u00b2=0.44)"
    assert clean_latex_artifacts("10^6 samples") == "10\u2076 samples"


def test_footnote_balanced_removed_unterminated_keeps_text():
    balanced = r"robust reasoning.\footnote{See https://example.com for details.} We conclude."
    assert clean_latex_artifacts(balanced) == "robust reasoning. We conclude."
    unterminated = "improves robustness.\\footnote{The code and data are available: https://github.com/X/Y."
    assert (
        clean_latex_artifacts(unterminated)
        == "improves robustness. The code and data are available: https://github.com/X/Y."
    )


def test_idempotent_and_whitespace():
    once = clean_latex_artifacts(r"\textbf{A } \emph{b}  double")
    assert clean_latex_artifacts(once) == once == "A b double"


def test_empty_and_clean_strings_untouched():
    assert clean_latex_artifacts("") == ""
    assert clean_latex_artifacts(None) is None
    assert clean_latex_artifacts("Plain abstract, no artifacts.") == "Plain abstract, no artifacts."
