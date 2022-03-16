"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from spaceflights.pipelines.data_engineering import pipeline as de
from spaceflights.pipelines.data_science import pipeline as ds


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    de_pipeline = de.create_pipeline()
    ds_pipeline = ds.create_pipeline()

    return {
    	"de": de_pipeline,
    	"ds": ds_pipeline,
    	"__default__": de_pipeline + ds_pipeline
    }
