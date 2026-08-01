from services.vectorstore import index


def reset_index():
    print("Current Pinecone index:")
    print(index.describe_index_stats())

    confirmation = input(
        "\nThis will DELETE ALL vectors from the Pinecone index.\n"
        "Type DELETE to continue: "
    )

    if confirmation != "DELETE":
        print("Reset cancelled.")
        return

    print("\nDeleting existing vectors...")

    index.delete(delete_all=True)

    print("✅ All vectors deleted.")

    print("\nUpdated index stats:")
    print(index.describe_index_stats())


if __name__ == "__main__":
    reset_index()