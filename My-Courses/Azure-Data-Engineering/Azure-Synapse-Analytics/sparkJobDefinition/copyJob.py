import sys
from pyspark.sql import SparkSession

# -----------------------------
# Step 1: Validate Arguments
# -----------------------------
if len(sys.argv) != 3:
    print("Usage: script.py <source_path> <destination_path>")
    sys.exit(1)

source_path = sys.argv[1]
destination_path = sys.argv[2]

print(f"Source: {source_path}")
print(f"Destination: {destination_path}")

# -----------------------------
# Step 2: Create Spark Session
# -----------------------------
spark = SparkSession.builder.appName("CopyDataJob").getOrCreate()

# -----------------------------
# Step 3: Read Data
# (Assuming CSV — can change)
# -----------------------------
df = spark.read.option("header", "true").csv(source_path)

print("Data Preview:")
df.show(5)

# -----------------------------
# Step 4: Write Data
# -----------------------------
df.write.mode("overwrite").option("header", "true").csv(destination_path)

print("Data copied successfully!")

# -----------------------------
# Step 5: Stop Spark Session
# -----------------------------
spark.stop()