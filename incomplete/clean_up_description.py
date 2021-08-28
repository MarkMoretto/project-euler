
"""
Purpose: Clean-up Projec-Euler problem description.
Date created: 2021-08-08

Contributor(s):
    Mark M.

"""

import re

# Description in HTML format
desc="""
<p>The numbers $545$, $5\,995$ and $15\,151$ are the three smallest <b>palindromes</b>
divisible by $109$. There are nine palindromes less than $100\,000$ which are divisible
by $109$.</p>

<p>How many palindromes less than $10^{32}$ are divisible by $10\,000\,019\,$ ?</p>
""".strip()


ptrn = r"""
    (</?\w+>+)
    |(\\,)
    |(?<=\d|,)(\$)
    |(\$)(?=\d)
"""

p = re.compile(ptrn, flags = re.I | re.M | re.X)


def cleaner(description: str) -> str:
    """Returns cleaned-up description for a given project-euler problem.

    Parameters
    ----------
    description : str
        The problem description in HTML format.
    
    Returns
    -------
    str
        The problem description with fewer markup indicators.
    """
    _desc = p.sub("", description)
    
    _desc = re.sub(r"\^\{(\d+)\}\$", r"**\1", _desc)
    
    _desc = re.sub(r"\s+?(?=\?$)", "", _desc)
    
    return _desc

