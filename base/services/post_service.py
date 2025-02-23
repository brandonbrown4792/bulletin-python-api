from base.models.post import Post

def create_post(data):
    try:
        # Create a new post in the database
        post = Post.objects.create(**data)
        return post
    except KeyError as e:
        raise ValueError(f'Missing required field: {e}')
    except Exception as e:
        # Handle other potential errors
        raise Exception(f'Error while adding post: {e}')