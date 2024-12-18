# model_checker
Compare the quality of two models

# Components

# Metadata
    -name
    -uri
    -version
    -tags
    -created
    -last_updated

## ModelWrapper
- name
- version
- uri
- last_updated
- tags

## ModelFactory

## Dataset_Information
    - uri
    - name
    - version
    - description
    - size

## Dataset
    - 

## Test_Conditions
    - Dataset_information
    - Model

## Result

## Metric
    - name
    - how to calcualte via interface
    - specific parameters

## MetricEngine
    - Produce Metrics Sets

## Evaluator
    - Evaluates the Set of Metrics on the dataset

# Evaluation (Test)
    - Model
    - Test_Conditions
    - Result

## Comparator
    - Compare Evaluations
        - Base On Test Condtions
        - Models
        - Results

# Visual_Graph
    

## Visualizer
    - Evaluation
    -