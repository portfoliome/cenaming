# cenaming
Company legal name normalization and shortening

# Description
Censible believes simplifying finance helps promote greater financial literacy, enabling investors to strive for sustainable, long-term investment objectives and goals. In our [company profile lookup](https://esg.censible.co/companies), we were dissatisfied with the typical jargon associated with company legal names.

While cenaming unfortunately can't contain our whole simplification and normalization process of company legal names we get from Factset, this micro-package of code can be used as a cornerstone to removing the typical jargon. The remaining steps we undertake are some algorithmic comparisons to Factset's defined short company names, and these simplified names. We then compare potential name duplication to avoid url clashes, run a tie-breaking algorithm incorporating things like company size and locality and voila: simplified company names.

## Example
```python
from cenaming.name_shortener import remove_org_descriptors


simple_name = remove_org_descriptors('The Priceline Group, Inc.')
simple_name = remove_org_descriptors('Vodafone Group Plc)
```

## Package Installation
There are no external dependencies, and we would expect the code to run for most Python versions, but 3.5 or greater is recommended.

```bash
pip install cenaming
```
