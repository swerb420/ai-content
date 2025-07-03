PLATFORM_SCHEMAS = {
    "linkedin": """
    {
      \"type\": \"object\",
      \"properties\": {
        \"post\": {\"type\": \"string\"},
        \"call_to_action\": {\"type\": \"string\"}
      }
    }
    """,
    "xtwitter": """
    {
      \"type\": \"object\",
      \"properties\": {
        \"post\": {\"type\": \"string\"},
        \"hashtags\": {\"type\": \"array\", \"items\": {\"type\": \"string\"}}
      }
    }
    """
    # Add other platforms as needed
}
