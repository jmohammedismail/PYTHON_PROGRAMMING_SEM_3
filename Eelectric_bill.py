print("-----ELECTRICITY BILL------")
Cname=input("Enter the name :")
Cid=int(input("Enter the customers id :"))
PMR=float(input("Enter the PMR :"))
CMR=float(input("Enter the CMR :"))
Costperunit=float(input("Enter the cost per unit :"))
TUC=CMR-PMR
Energycharge=TUC*Costperunit
ElectricDuty=0.05*Energycharge
NetBill=Energycharge+ElectricDuty+100
print("NETBILL is :",NetBill)
