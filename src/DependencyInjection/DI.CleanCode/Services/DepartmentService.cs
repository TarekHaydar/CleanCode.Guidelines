namespace DI.CleanCode.Services
{
    using DI.CleanCode.Interfaces;
    using System.Collections.Generic;
    using System.Linq;

    public class DepartmentService : IDepartmentService
    {
        private readonly List<DepartmentInfo> departments = new List<DepartmentInfo>
        {
            new DepartmentInfo("Dev", "Development"),
            new DepartmentInfo("Acc", "Accounting"),
        };

        public DepartmentInfo GetDepartment(string code)
        {
            return departments.SingleOrDefault(o => o.Code == code);
        }
    }
}
