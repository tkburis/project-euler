import time


# https://www.blog.pythonlibrary.org/2016/05/24/python-101-an-intro-to-benchmarking-your-code/
class Timer:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        runtime = end - self.start
        msg = f"This function took {runtime} seconds to complete"
        print(msg)


if __name__ == "__main__":
    def long_runner():
        time.sleep(2)

    with Timer():
        long_runner()
