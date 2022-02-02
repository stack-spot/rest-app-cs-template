from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata
import subprocess

class RestTemplate(Template):

    def pre_hook(self, metadata: Metadata) -> Metadata:
        print('Installing stackspot.rest...')
        args = ['dotnet', 'new', '-i', 'StackSpot.Template.Rest', '--force']
        subprocess.run(args)
        
        return metadata

    def post_hook(self, metadata: Metadata):
        project_name = metadata.inputs['project_name']
        args = ['dotnet', 'new', 'stackspot.rest', '-n', project_name, '-p', project_name, '--force']
        
        print('Creating application...')
        subprocess.run(args)
        print('Application Created.')

if __name__ == '__main__':
    run(RestTemplate())