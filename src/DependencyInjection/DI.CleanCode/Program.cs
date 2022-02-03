using DI.CleanCode.Interfaces;
using DI.CleanCode.Services;
using Microsoft.Extensions.DependencyInjection;
using System;

namespace DI.CleanCode
{
    class Program
    {
        static void Main(string[] args)
        {
            // first example - tightly coupled
            //var employeeService = new EmployeeServiceTightlyCoupled();
            //Console.WriteLine(employeeService.CreateEmployee(new CreateEmployeeObjectModel
            //{
            //    Name = "Tarek Haydar",
            //    DepartmentCode = "Dev",
            //    DateOfBirth = new DateTime(1990,11,1)
            //}));

            // second example - loosely coupled
            //var employeeService = new EmployeeServiceLooselyCoupled(new DepartmentService());
            //Console.WriteLine(employeeService.CreateEmployee(new CreateEmployeeObjectModel
            //{
            //    Name = "Tarek Haydar",
            //    DepartmentCode = "Dev",
            //    DateOfBirth = new DateTime(1990, 11, 1)
            //}));

            // third example - loosely coupled with DI
            var serviceProvider = new ServiceCollection()
            .AddSingleton<IDepartmentService, DepartmentService>()
            .AddSingleton<IEmployeeService, EmployeeServiceLooselyCoupled>()
            .BuildServiceProvider();

            var employeeService = serviceProvider.GetService<IEmployeeService>();
            Console.WriteLine(employeeService.CreateEmployee(new CreateEmployeeObjectModel
            {
                Name = "Tarek Haydar",
                DepartmentCode = "Dev",
                DateOfBirth = new DateTime(1990, 11, 1)
            }));

        }
    }
}
