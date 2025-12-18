# EXERCISE 1

## Part 1: Kubernetes deployment object
### JQ Pattern

.spec.replicas

.spec.strategy.type

.metadata.labels.service + "-" + .metadata.labels.environment

## Part 2: Jira API issue response
### JQ Pattern

[.fields.subtasks[].key]

## Explanation
I treated both responses as JSON trees. For Kubernetes, I navigated through spec and metadata to extract replicas, strategy, and labels. For Jira, I iterated over the subtasks array and extracted each issue key.
