from app.cv_reader import read_text_file
from app.evaluator import evaluate_cv


def main():
    cv_text = read_text_file("inputs/cv.txt")
    job_requirements = read_text_file("inputs/job_requirements.txt")

    result = evaluate_cv(cv_text, job_requirements)

    print("\n=== CV EVALUATION RESULT ===")
    print(f"Aplica: {'Sí' if result.applies else 'No'}")
    print(f"Score: {result.score}/100")
    print(f"Veredicto: {result.verdict}")

    print("\nFortalezas:")
    for strength in result.strengths:
        print(f"- {strength}")

    print("\nGaps:")
    for gap in result.gaps:
        print(f"- {gap}")

    print("\nRecomendación:")
    print(result.recommendation)


if __name__ == "__main__":
    main()