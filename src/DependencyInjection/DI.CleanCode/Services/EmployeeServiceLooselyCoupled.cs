namespace DI.CleanCode.Services
{
    using DI.CleanCode.Interfaces;

    public class EmployeeServiceLooselyCoupled : IEmployeeService
    {
        private readonly IDepartmentService departmentService;

        public EmployeeServiceLooselyCoupled(IDepartmentService departmentService)
        {
            this.departmentService = departmentService;
        }

        public int CreateEmployee(CreateEmployeeObjectModel objectModel)
        {
            //some code here

            var department = departmentService.GetDepartment(objectModel.DepartmentCode);

            return 10;
        }
    }
}