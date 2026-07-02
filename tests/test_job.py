from job_processor import create_job_embedding

job_text, embedding = create_job_embedding()

print("=" * 60)
print("JOB DESCRIPTION")
print("=" * 60)

print(job_text[:1000])      # Print first 1000 characters

print("\n")
print("=" * 60)
print("EMBEDDING INFO")
print("=" * 60)

print("Embedding Length:", len(embedding))
print("First 10 Numbers:")

print(embedding[:10])