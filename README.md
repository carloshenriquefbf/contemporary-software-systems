## Instructions

1.  Set Up Google Custom Search API
    - Create a Google Custom Search Engine (CSE):

    - Go to: https://programmablesearchengine.google.com/

    - Click “Add” to create a new search engine.

    - Set it to search the entire web (in control panel: tick "Search the entire web").

2. Get API Key:

    - Go to https://console.cloud.google.com/apis

    - Create a new project (or use an existing one).

    - Enable the Custom Search API for the project.

    - Go to "Credentials" and create an API key.

3. Set Up Environment Variables

    - Create a `.env` file in the root directory of your project.

    - Add the following lines to the `.env` file:

    ```plaintext
    API_KEY=your_google_api_key
    CSE_ID=your_google_cse_id
    ```
4. Run the `google.py` script modifying the `query` variable to search for the `websites_to_exclude` and/or `websites_to_include` variables.

## Query example:

```python
    # google
    "software engineering"
    AND (
        "test" OR "quality" OR "validation" OR "verification" OR "technical debt" OR "defect detection" OR "software inspection" OR "model checking" OR "debug" OR "code review"
    ) AND (
        "Generative AI" OR "Generative Artificial Intelligence"  OR "Large Language Model"  OR "LLM"
    ) after:2021 -site:youtube.com -site:github.com -site:paperswithcode.com

    # github
    "software engineering"
    AND (
        "test" OR "quality" OR "validation" OR "verification" OR "technical debt" OR "defect detection" OR "software inspection" OR "model checking" OR "debug" OR "code review"
    ) AND (
        "Generative AI" OR "Generative Artificial Intelligence"  OR "Large Language Model"  OR "LLM"
    ) after:2021 site:github.com

    # papers with code
    "software engineering"
    AND (
        "test" OR "quality" OR "validation" OR "verification" OR "technical debt" OR "defect detection" OR "software inspection" OR "model checking" OR "debug" OR "code review"
    ) AND (
        "Generative AI" OR "Generative Artificial Intelligence"  OR "Large Language Model"  OR "LLM"
    ) after:2021 site:paperswithcode.com/paper
```
