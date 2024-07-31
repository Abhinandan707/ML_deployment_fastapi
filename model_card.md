# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model created by Chirag Dudhat

Model use `RandomForestClassifier` from `sklearn.model.RandomForestClassifier` for classification tasks.

The parameters used are default.

## Intended Use
This model predicts whether a person earns over 50k or not based on the census data.

## Training Data
More details about the training data: https://archive.ics.uci.edu/ml/datasets/census+income

Extraction was done by Barry Becker from the 1994 Census database.

Prediction task is to determine whether a person makes over 50K a year.

Features:

- **Age**: Continuous variable representing the age of the individual.
- **Workclass**: Categorical variable with the following categories: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
- **Fnlwgt**: Continuous variable representing the final weight.
- **Education**: Categorical variable with the following categories: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
- **Education-num**: Continuous variable representing the number of years of education.
- **Marital-status**: Categorical variable with the following categories: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
- **Occupation**: Categorical variable with the following categories: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
- **Relationship**: Categorical variable with the following categories: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
- **Race**: Categorical variable with the following categories: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
- **Sex**: Categorical variable with the following categories: Female, Male.
- **Capital-gain**: Continuous variable representing capital gain.
- **Capital-loss**: Continuous variable representing capital loss.
- **Hours-per-week**: Continuous variable representing hours worked per week.
- **Native-country**: Categorical variable with the following categories: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinidad & Tobago, Peru, Hong Kong, Netherlands.

For both training and evaluation, categorical features are encoded using the `OneHotEncoder`, and the target variable is transformed using the `LabelBinarizer`.


## Evaluation Data
The original dataset is first preprocessed and then split into training and evaluation data with evaluation data size of 20%

## Metrics
Performances of the model:
- precision: 0.7169206094627105
- recall: 0.6056910569105691
- fbeta: 0.6566287183253764

## Ethical Considerations
This model is trained on census data. The model is not biased towards any particular group of people.

## Caveats and Recommendations
I'd urge the user that checks are included upstream of any decision-making points to ensure that bias is minimized.