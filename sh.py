contents = ""
for i in range(1000):
    contents += f"""gsutil -m cp "gs://dataset_reddit/reddit/20220806/train-{i:05}-of-01000.json" data/train/.\n"""
    contents += f"""gsutil -m cp "gs://dataset_reddit/reddit/20220806/test-{i:05}-of-01000.json" data/train/.\n"""

open("run.sh", 'w').write(contents)