# ARGENT: n(AR)rative (G)raph g(EN)era(T)ion
This project is intended to explore LLM-enabled approaches for knowledge graph generation to understand long form fiction. This framining provides several unique challenges not easily addressed by existing tools, data, and evaluation metrics. Where a human can read a story and understand the characters, settings, and events, approaches for automatic summarization, reading comprehensions, and other tools often fall short of providing useful insights. 

## Capability Goals
Ideally, the capabilities developed here will be able to answer the following:
1. Who are the characters? Physical descriptions? Connections to other characters?
2. What are the settings? Description? Connections to other settings?
3. How to characters move through time? What is their path through settings? How do their connections with characters change?
4. How do character beliefs change over time?
5. For a given section of text (scene, chapter, etc.), what happened? (summarize)

In support of these goals, we should also enable:
1. Provenance; when insights are derived from text, they should be sourced to the original content
2. Query and visualization; we should be able to see how characters / settings change over time
