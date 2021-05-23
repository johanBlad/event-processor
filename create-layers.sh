cd lambdas/layers/generator-deps/
rm -rf ./python; rm python.zip
pip install -r requirements.txt -t ./python --upgrade; cp -r ../../common ./python
zip -r python.zip python/

cd ../processor-deps/
rm -rf ./python; rm python.zip
pip install -r requirements.txt -t ./python --upgrade; cp -r ../../common ./python
zip -r python.zip python/