# Databricks notebook source
mf_workspace_id = "<your_workspace_id>"
mf_lakehouse_id "<lakehouse_id>"
mf_table = "<table_name>"

ms_dim_date_df = spark.read.format("delta").load(f"abfss://{mf_workspace_id}@onelake.dfs.fabric.microsoft.com/{mf_lakehouse_id}/Tables/{mf_table}")
