
from collections import namedtuple


DataIngestionConfig=namedtuple("DataIngestionConfig",
["detaset_downlod_url","tgz_download_dir","raw_data_dir",'íngested_train_dir',"ingested_test_dir"])


DataValidationConfig=namedtuple("DataValidationConfig",["schema_file_path"])


DataTransformationConfig=namedtuple("DataTransformationConfig",["add_bedroom_per_room",
                                                                 "transformed_train_dir" ,
                                                                 "transformed_test_dir",
                                                                 "preprocessed_object_file_path"])

ModelTrianConfig=namedtuple("ModelTrianConfig",["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig=namedtuple("ModelEvaluationconfig",['model_evaluation_file_path',"time_stamp"])

ModelPusherConfig=namedtuple("ModelPusherConfig",["export_dir_path"])

TrainingPipelineCofig=namedtuple("TrainingPipelineCofig",["artifact_dir"])
