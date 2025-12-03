def employee_info(name: str, emp_id: str, department: str, salary: float) -> str:
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary:.2f}"
    )
if __name__ == "__main__":
    # Example usage
    print(employee_info("Harsha", "H228", "Finance",70000))