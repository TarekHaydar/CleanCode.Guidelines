using System;

namespace DI.CleanCode.Interfaces
{
    public interface IEmployeeService
    {
        int CreateEmployee(CreateEmployeeObjectModel objectModel);
    }

    public class CreateEmployeeObjectModel
    {
        public string Name { get; set; }
        public DateTime DateOfBirth { get; set; }
        public string DepartmentCode { get; set; }
    }
}
