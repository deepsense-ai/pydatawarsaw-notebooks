pip install virtualenv
virtualenv -p python3 ~/.env_jp_nb
source ~/.env_jp_nb/bin/activate

pip install -r requirements.txt

jt -t oceans16 -T
cp resources/deepsensify.css ~/.jupyter/custom/custom.css

jupyter-contrib nbextension install --sys-prefix

python -m ipykernel install --user --name env_jp_nb --display-name "awesome_notebooks"