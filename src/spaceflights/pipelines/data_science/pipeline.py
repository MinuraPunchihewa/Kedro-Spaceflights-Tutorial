from kedro.pipeline import node, Pipeline
from spaceflights.pipelines.data_science.nodes import split_data, train_model, evaluate_model

def create_pipeline(**kwargs):
	return Pipeline(
		[
			node(
				func=split_data,
				inputs=["master_table", "parameters"],
				outputs=["x_train", "x_test", "y_train", "y_test"],
				name="split_data"
			),
			node(
				func=train_model,
				inputs=["x_train", "y_train"],
				outputs="regressor"
			),
			node(
				func=evaluate_model,
				inputs=["regressor", "x_test", "y_test"],
				outputs=None
			)
		]
	)