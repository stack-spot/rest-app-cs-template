from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata
import subprocess

class RestTemplate(Template):

    def pre_hook(self, metadata: Metadata) -> Metadata:
        print('Installing stackspot.rest...')
        args = ['dotnet', 'new', '-i', 'StackSpot.Template.Rest', '--force']
        subprocess.run(args)
        
        print('Installing dotnet-format...')
        args2 = ['dotnet', 'tool', 'install', '-g', 'dotnet-format']
        subprocess.run(args2)

        return metadata

    def post_hook(self, metadata: Metadata):
        project_name = metadata.global_inputs['project_name']
        args = ['dotnet', 'new', 'stackspot.rest', '-n', project_name, '-p', project_name, '--skipRestore', 'true', '--force', '-o', metadata.target_path]
        
        print('Creating application...')
        subprocess.run(args)
        print('Application Created.')

if __name__ == '__main__':
    run(RestTemplate())