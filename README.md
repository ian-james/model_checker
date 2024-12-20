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

# Timing
  - Time Started
  - Time Finished

# Parameters

## ModelWrapper
- name
- short_name
- model
- comment


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

    - Example 
    - TestName
    - Phase
    - Data
    - Result

    ex){ name="Test1", phase="train", test_params={'cross-validation'}, result={'accuracy'=0.8}

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