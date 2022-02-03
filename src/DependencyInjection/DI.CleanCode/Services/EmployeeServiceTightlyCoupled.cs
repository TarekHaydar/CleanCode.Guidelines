namespace DI.CleanCode.Services
{
    using DI.CleanCode.Interfaces;

    public class EmployeeServiceTightlyCoupled : IEmployeeService
    {
        public int CreateEmployee(CreateEmployeeObjectModel objectModel)
        {
            //some code here

            var departmentService = new DepartmentService();
            var department = departmentService.GetDepartment(objectModel.DepartmentCode);

            return 10;
        }
    }
}
