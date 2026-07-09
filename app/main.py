from app.pipeline import CareerPipeline


def main():

    pipeline = CareerPipeline()

    candidate = pipeline.run(
        "resumes/sample_resume.pdf"
    )

    print(candidate.get_profile())


if __name__ == "__main__":
    main()