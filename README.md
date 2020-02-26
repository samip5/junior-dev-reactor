## How to set it up?

1. Download/clone the repository to your local machine.
2. Install Docker if you don't have it yet.
3. Run in the main cloned directory: `sudo docker build -t samip537/junior-dev .` to build the Docker image.
4. Create and run the container by executing:
`sudo docker create --name junior-dev-sm samip537/junior-dev:latest ` and then to run it: `sudo docker start junior-dev-sm`.
5. It should be accessible on port 80 at 127.0.0.1:80, if not check logs.

## Why is it missing some things?

Due to the fact that I couldn't figure those out as I needed to balance between doing this and school assignments.  
