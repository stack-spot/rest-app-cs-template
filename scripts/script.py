from templateframework.metadata import Metadata
def run(metadata: Metadata = None):
    metadata.global_inputs['project_type'] = 'Api'
    return metadata