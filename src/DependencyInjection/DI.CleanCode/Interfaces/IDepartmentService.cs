namespace DI.CleanCode.Interfaces
{
    public interface IDepartmentService
    {
        DepartmentInfo GetDepartment(string code);
    }

    public class DepartmentInfo
    {
        public DepartmentInfo(string code, string name)
        {
            Code = code;
            Name = name;
        }

        public string Code { get; }
        public string Name { get; }
    }
}
