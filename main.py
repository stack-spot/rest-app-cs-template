from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata
import subprocess
import sys

class RestTemplate(Template):

    def pre_hook(self, metadata: Metadata) -> Metadata:
        print('Installing stackspot.rest...')
        args = [metadata.target_path, 'dotnet new -i StackSpot.Template.Rest --force']
        subprocess.run(args)
        
        return metadata

    def post_hook(self, metadata: Metadata):
        project_name = metadata.inputs['project_name']
        args = [metadata.target_path, 'dotnet new stackspot.rest -n sys.stdin.read() -p sys.stdin.read() --force']
        
        print('Creating application...')
        subprocess.run(args, input=project_name)
        print('Application Created.')

if __name__ == '__main__':
    run(RestTemplate())