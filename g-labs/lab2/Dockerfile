FROM alpine:3.18

# 1. Create a dedicated non-root group and user
# -S flag creates a system account (no home directory/login shell) for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# 2. Set the working directory
WORKDIR /app

# 3. Create a test file, initially owned by root (default user)
RUN echo "Hello, Root!" > test-file-by-root.txt

# 4. Change ownership of the app directory to the new non-root user
# This is crucial so the non-root user can write/read/execute here
RUN chown -R appuser:appgroup /app

# 5. Switch to the non-root user for all subsequent instructions
USER appuser

# 6. Try to create a new file as the non-root user
RUN echo "Hello, Non-Root!" > test-file-by-nonroot.txt

# Final command: list contents and show user ID
CMD ["sh", "-c", "whoami && ls -l && cat test-file-by-nonroot.txt"]