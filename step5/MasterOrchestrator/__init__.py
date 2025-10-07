import os
import json
import logging
import azure.durable_functions as df
import itertools

def orchestrator_function(context: df.DurableOrchestrationContext):
    connect_str = os.environ.get("BlobStorageConnectionString")
    container_name = "containerlab5"
    
    # Read input data from blob storage
    data = yield context.call_activity("GetInputDataFn", (connect_str, container_name))
    #data = ['Thank you for the music', 'Welcome to the jungle']
    logging.info(f"data = '{data}'.")

    # Call mapper function for each line of input data
    tasks = []
    for kv_pair in data:
        tasks.append(context.call_activity("MapperFunction", kv_pair))
    map_output = yield context.task_all(tasks)
    map_output = list(itertools.chain.from_iterable(map_output))
    logging.info(f"map_output = '{map_output}'.")

    # Call shuffler function to prepare data for reducer
    logging.info(f"Sending '{map_output}' to shuffler.")
    shuffle_output = yield context.call_activity("ShufflerFunction", map_output)
    logging.info(f"shuffle_output = '{shuffle_output}'.")

    # Call reducer function for each key in shuffle output
    tasks = []
    for kv_pair in shuffle_output:
        tasks.append(context.call_activity("ReducerFunction", kv_pair))
    reduce_output = yield context.task_all(tasks)
    logging.info(f"reduce_output = '{reduce_output}'.")

    # Return reduce output as JSON
    return json.dumps(reduce_output)

main = df.Orchestrator.create(orchestrator_function)