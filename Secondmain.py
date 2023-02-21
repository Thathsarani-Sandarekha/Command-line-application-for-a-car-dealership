while True:
    def options(option=None, position=None):
        position = int(
            input("\t1.Admin\n\t2.Customer\n\t3.Owner\n\t4.Technician\nPlease insert your position Number:\n"))
        if position == 1:
            admin()
        elif position == 2:
            customer()
        elif position == 3:
            owner()
        elif position == 4:
            technician()
        else:
            print("Invalid input")


    def admin():
        print("1. Enter New Car Details")
        print("2. Edit Car Information")
        print("3. Change Car Status")
        print("4. Check Appointments")
        print("5. Approve Customer Requests")
        tasks = int(input("Choose an option: "))

        if tasks == 1:
            add_new_car()
        elif tasks == 2:
            edit_car_info()
        elif tasks == 3:
            change_car_status()
        elif tasks == 4:
            check_appointments()
        elif tasks == 5:
            allow_test_drives()
        else:
            print("Enter a valid input")


    def add_new_car():
        car_details = open("Car Details.txt", "a")

        index = input("Index Number: ")
        the_make = input("The make: ").capitalize()
        model = input("Model: ").capitalize()
        mileage = input("Mileage: ")
        colour = input("Colour: ").capitalize()
        year = input("Year: ")
        condition = input("Condition: ").capitalize()
        car_states = input("Car Status: ").capitalize()

        if len(index and the_make and model and mileage and colour and year and condition and car_states) < 1:
            print("Something went wrong. Please fill all the details and try again")

        else:
            if car_states == "available" or "sold":
                car_details.write(index + " , " + the_make + " , " + model + " , " + mileage + " , " + colour
                                  + " , " + year + " , " + condition + " , " + car_states + "\n")
                print("The new car details successfully added!")

            else:
                print("Please enter a valid input for car status.")

        owner_info = open("Owner Information.txt", "a")

        owner_name = input("Owner information: \n\tOwner Name: ").capitalize()
        owner_contact = input("\tContact number: ")
        owner_city = input("\tCity: ").capitalize()

        if len(owner_name and owner_contact and owner_city) < 1:
            print("Please fill all the details and try again")

        else:
            owner_info.write(index + " , " + owner_name + " , " + owner_contact + " , " + owner_city + "\n")
            print("Owner Information Successfully added!")

        pricing_info = open("Car Pricing Details.txt", "a")

        asking_price = input("Asking Price: Rs:")
        selling_price = input("Selling Price: Rs:")

        if len(asking_price and selling_price) < 1:
            print("Please fill all the details and try again")

        else:
            pricing_info.write(index + " , " + asking_price + " , " + selling_price + "\n")
            print("Pricing information Successfully added!")


    def edit_car_info():
        print("1. The make: ")
        print("2. Model: ")
        print("3. Mileage: ")
        print("4. Colour: ")
        print("5. Year: ")
        print("6. Condition: ")
        print("7. Owner Name: ")
        print("8. Owner Contact Number: ")
        print("9.Owner City: ")
        print("10.Asking Price: ")
        print("11.Selling Price: ")

        record = int(input("Enter the record number that you want to edit: "))

        if record == 1:
            make()
        elif record == 2:
            model()
        elif record == 3:
            mileage()
        elif record == 4:
            colour()
        elif record == 5:
            year()
        elif record == 6:
            condition()
        elif record == 7:
            owner_name()
        elif record == 8:
            owner_contact()
        elif record == 9:
            owner_city()
        elif record == 10:
            asking_price()
        elif record == 11:
            selling_price()
        else:
            print("Please enter a valid input")
            edit_car_info()


    def make():
        car_details = open("Car Details.txt", "r")

        ind = []
        tm = []
        mo = []
        mi = []
        cl = []
        yr = []
        con = []
        cs = []

        for i in car_details:
            a, b, c, d, e, f, g, h = i.split(" , ")
            ind.append(a)
            tm.append(b)
            mo.append(c)
            mi.append(d)
            cl.append(e)
            yr.append(f)
            con.append(g)
            cs.append(h)

            index_with_make = dict(zip(ind, tm))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_make[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_make[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    make()
        except:
            print("index number doesn't exist")


    def model():
        car_details = open("Car Details.txt", "r")

        ind = []
        tm = []
        mo = []
        mi = []
        cl = []
        yr = []
        con = []
        cs = []

        for i in car_details:
            a, b, c, d, e, f, g, h = i.split(" , ")
            ind.append(a)
            tm.append(b)
            mo.append(c)
            mi.append(d)
            cl.append(e)
            yr.append(f)
            con.append(g)
            cs.append(h)

            index_with_model = dict(zip(ind, mo))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_model[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_model[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    model()
        except:
            print("index number doesn't exist")


    def mileage():
        car_details = open("Car Details.txt", "r")

        ind = []
        tm = []
        mo = []
        mi = []
        cl = []
        yr = []
        con = []
        cs = []

        for i in car_details:
            a, b, c, d, e, f, g, h = i.split(" , ")
            ind.append(a)
            tm.append(b)
            mo.append(c)
            mi.append(d)
            cl.append(e)
            yr.append(f)
            con.append(g)
            cs.append(h)

            index_with_mileage = dict(zip(ind, mi))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_mileage[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_mileage[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    mileage()
        except:
            print("index number doesn't exist")


    def colour():
        car_details = open("Car Details.txt", "r")

        ind = []
        tm = []
        mo = []
        mi = []
        cl = []
        yr = []
        con = []
        cs = []

        for i in car_details:
            a, b, c, d, e, f, g, h = i.split(" , ")
            ind.append(a)
            tm.append(b)
            mo.append(c)
            mi.append(d)
            cl.append(e)
            yr.append(f)
            con.append(g)
            cs.append(h)

            index_with_colour = dict(zip(ind, cl))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_colour[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_colour[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    colour()
        except:
            print("index number doesn't exist")


    def year():
        car_details = open("Car Details.txt", "r")

        ind = []
        tm = []
        mo = []
        mi = []
        cl = []
        yr = []
        con = []
        cs = []

        for i in car_details:
            a, b, c, d, e, f, g, h = i.split(" , ")
            ind.append(a)
            tm.append(b)
            mo.append(c)
            mi.append(d)
            cl.append(e)
            yr.append(f)
            con.append(g)
            cs.append(h)

            index_with_year = dict(zip(ind, yr))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_year[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_year[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    year()
        except:
            print("index number doesn't exist")


    def condition():
        car_details = open("Car Details.txt", "r")

        ind = []
        tm = []
        mo = []
        mi = []
        cl = []
        yr = []
        con = []
        cs = []

        for i in car_details:
            a, b, c, d, e, f, g, h = i.split(" , ")
            ind.append(a)
            tm.append(b)
            mo.append(c)
            mi.append(d)
            cl.append(e)
            yr.append(f)
            con.append(g)
            cs.append(h)

            index_with_condition = dict(zip(ind, con))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_condition[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_condition[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    condition()
        except:
            print("index number doesn't exist")


    def owner_name():
        owner_info = open("Owner Information.txt", "r")

        ind = []
        on = []
        oc = []
        oci = []

        for i in owner_info:
            a, b, c, d = i.split(" , ")
            ind.append(a)
            on.append(b)
            oc.append(c)
            oci.append(d)

            index_with_o_name = dict(zip(ind, on))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_o_name[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_o_name[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Owner Information.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Owner Information.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    owner_name()
        except:
            print("index number doesn't exist")


    def owner_contact():
        owner_info = open("Owner Information.txt", "r")

        ind = []
        on = []
        oc = []
        oci = []

        for i in owner_info:
            a, b, c, d = i.split(" , ")
            ind.append(a)
            on.append(b)
            oc.append(c)
            oci.append(d)

            index_with_o_contact = dict(zip(ind, oc))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_o_contact[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_o_contact[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Owner Information.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Owner Information.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    owner_name()
        except:
            print("index number doesn't exist")


    def owner_city():
        owner_info = open("Owner Information.txt", "r")

        ind = []
        on = []
        oc = []
        oci = []

        for i in owner_info:
            a, b, c, d = i.split(" , ")
            ind.append(a)
            on.append(b)
            oc.append(c)
            oci.append(d.strip())

            index_with_o_city = dict(zip(ind, oci))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_o_city[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_o_city[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Owner Information.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Owner Information.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    owner_city()
        except:
            print("index number doesn't exist")


    def asking_price():
        pricing_info = open("Car Pricing Details.txt", "r")

        ind = []
        ap = []
        sp = []

        for i in pricing_info:
            a, b, c = i.split(" , ")
            ind.append(a)
            ap.append(b)
            sp.append(c)

            index_with_ask = dict(zip(ind, ap))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_ask[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_ask[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Pricing Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Pricing Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    owner_name()
        except:
            print("index number doesn't exist")


    def selling_price():
        pricing_info = open("Car Pricing Details.txt", "r")

        ind = []
        ap = []
        sp = []

        for i in pricing_info:
            a, b, c = i.split(" , ")
            ind.append(a)
            ap.append(b)
            sp.append(c.strip())

            index_with_selling = dict(zip(ind, sp))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_selling[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_selling[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Pricing Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Pricing Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    owner_name()
        except:
            print("index number doesn't exist")


    def change_car_status():
        car_details = open("Car Details.txt", "r")

        ind = []
        tm = []
        mo = []
        mi = []
        cl = []
        yr = []
        con = []
        cs = []

        for i in car_details:
            a, b, c, d, e, f, g, h = i.split(" , ")
            ind.append(a)
            tm.append(b)
            mo.append(c)
            mi.append(d)
            cl.append(e)
            yr.append(f)
            con.append(g)
            cs.append(h.strip())

            index_with_status = dict(zip(ind, cs))

        ask_index = input("Enter the index number of car that you want to edit the above car information: ")
        try:
            if index_with_status[ask_index]:
                search_text = input("Enter the record that you want to edit: ")
                if search_text == index_with_status[ask_index]:
                    replace_text = input("Enter the new record to be replaced: ")
                    with open("Car Details.txt", "r") as file:
                        data = file.read()
                        data = data.replace(search_text, replace_text)

                    with open("Car Details.txt", "w") as file:
                        file.write(data)

                    print("Record replaced successfully!")
                else:
                    print("select correct index number")
                    change_car_status()
        except:
            print("index number doesn't exist")


    def check_appointments():
        test_drive = open("Requests for Test Drive.txt", "r")

        ind = []
        name = []
        id = []

        for i in test_drive:
            a, b, c, d = i.split(" , ")
            ind.append(a)
            name.append(b)
            id.append(int(d.strip()))

            if len(id) != 0:
                print(len(id), "appointments requested."),
                print("Car index number: " + a),
                print("Requestor's name: " + b),
                print("Requestor's contact number: " + c),
                print("Requestor's NIC number: " + d)


    def allow_test_drives():
        test_drive = open("Requests for Test Drive.txt", "r")

        allow_test_drive = open("Allow Test Drives.txt", "a")

        not_allow_test_drive = open("Not allowed test drives.txt", "a")

        nic = []
        for j in test_drive:
            a, b, c, d = j.split(" , ")
            nic.append(int(d.strip()))

        checking_id = int(input("Enter the requestor NIC number: "))
        if checking_id in nic:
            allow = int(input("Do you want to allow this test drive?\n\t1.Yes\n\t2.No\n"))
            if allow == 1:
                allow_test_drive.write(str(checking_id) + " , " + "YES")
            elif allow == 2:
                not_allow_test_drive.write(str(checking_id) + " , " + "NO")


    def customer():
        print("1. Display Car Details....")
        print("2. Sort Cars")
        print("3. Request Test Drive")
        print("4. View Current Appointments Status")
        print("5. Buy a car")
        print("6. View Current Maintenance Information")

        select = input("Enter your choice :")
        if select == "1":
            display_cars()
        elif select == "2":
            sorting()
        elif select == "3":
            request_test_drive()
        elif select == "4":
            appointment_status()
        elif select == "5":
            buy_car()
        elif select == "6":
            maintenance_status()
        else:
            print("Please enter a valid input.")


    def display_cars():
        av = "Available"
        so = "Sold"

        car_details = open("Car Details.txt", "r")

        for i in car_details:
            a, b, c, d, e, f, g, h = i.split(" , ")
            if h.strip() == av:
                print("Index Number: " + a)

                print("Car Details")
                print("\tThe make: " + b)
                print("\tModel: " + c)
                print("\tMileage: " + d)
                print("\tColour: " + e)
                print("\tYear: " + f)
                print("\tCondition: " + g)

                owner_info = open("Owner Information.txt", "r")

                for j in owner_info:
                    k, l, m, n = j.split(" , ")
                    if k == a:
                        print("Owner Details")
                        print("\tOwner Name: " + l)
                        print("\tOwner Contact Number: " + m)
                        print("\tOwner City: " + n)

                        pricing_info = open("Car Pricing Details.txt", "r")

                        for r in pricing_info:
                            o, p, q = r.split(" , ")
                            if o == a:
                                print("Pricing Details")
                                print("\tSelling Price: " + q)

            elif h == so:
                print("SOLD")


    def request_test_drive():
        test_drive = open("Requests for Test Drive.txt", "a")

        ind = input("Index Number of the car: ")
        customer_name = input("Enter your name: ")
        customer_contact = input("Enter your contact number: ")
        customer_id = int(input("Enter your NIC number: "))

        if len(ind and customer_name and customer_contact) < 1:
            print("Something went wrong please try again.")
        else:
            test_drive.write(ind + " , " + customer_name + " , " + customer_contact + " , " + str(customer_id) + "\n")
            print("Your request successfully added! You can check the status while the admin respond to your request.")


    def appointment_status():
        test_drive = open("Requests for Test Drive.txt", "r")
        t_id = []

        for k in test_drive:
            p, q, r, s = k.split(" , ")
            t_id.append(int(s.strip()))

        allow_test_drive = open("Allow Test Drives.txt", "r")
        a_id = []
        a_allow = []

        for i in allow_test_drive:
            a, b = i.split(" , ")
            a_id.append(int(a))
            a_allow.append(b.strip())

        not_allow_test_drive = open("Not allowed test drives.txt", "r")
        n_id = []
        n_allow = []

        for j in not_allow_test_drive:
            c, d = j.split(" , ")
            n_id.append(int(c))
            n_allow.append(d.strip())

        checking_nic = int(input("Enter your NIC number: "))
        if checking_nic in t_id:
            if checking_nic in a_id:
                print("Admin has provide you an appointment")
            elif checking_nic in n_id:
                print("Admin has rejected your test drive.")
            else:
                print("Your appointment is pending...")
        else:
            print("Please request an appointment")


    def sorting():
        print("1.Sort By Budget")
        print("2.Sort By Mileage")
        select1 = input("Enter choice :")
        if select1 == "1":
            sort_budget()
        elif select1 == "2":
            sort_mileage()


    def sort_budget():
        budget_min = int(input("Enter the minimum budget that you want to sort? Rs: "))
        budget_max = int(input("Enter the maximum budget that you want to sort? Rs: "))

        pricing_info = open("Car Pricing Details.txt", "r")

        ind = []
        sp = []

        for i in pricing_info:
            a, b, c = i.split(" , ")
            ind.append(int(a))
            sp.append(int(c.strip()))

        for j in sp:
            if budget_min <= j <= budget_max:
                for k in ind:
                    if sp.index(j) == ind.index(k):
                        print(ind.index(k) + 1)
                        av = "Available"
                        so = "Sold"

                        car_details = open("Car Details.txt", "r")

                        for w in car_details:
                            d, e, f, g, h, l, m, n = w.split(" , ")
                            if str(ind.index(k) + 1) == d:
                                if n.strip() == av:
                                    print("Index Number: " + d)

                                    print("Car Details")
                                    print("\tThe make: " + e)
                                    print("\tModel: " + f)
                                    print("\tMileage: " + g)
                                    print("\tColour: " + h)
                                    print("\tYear: " + l)
                                    print("\tCondition: " + m)

                                    owner_info = open("Owner Information.txt", "r")

                                    for x in owner_info:
                                        s, t, u, v = x.split(" , ")
                                        if s == d:
                                            print("Owner Details")
                                            print("\tOwner Name: " + t)
                                            print("\tOwner Contact Number: " + u)
                                            print("\tOwner City: " + v)

                                            pricing_info = open("Car Pricing Details.txt", "r")

                                            for y in pricing_info:
                                                o, p, q = y.split(" , ")
                                                if o == d:
                                                    print("Pricing Details")
                                                    print("\tSelling Price: " + q)

            else:
                print("No vehicles available for this range")


    def sort_mileage():
        mil_min = int(input("Enter the minimum mileage that you want to sort:  "))
        mil_max = int(input("Enter the maximum mileage that you want to sort:  "))

        car_details = open("Car Details.txt", "r")

        ind = []
        mi = []

        for i in car_details:
            ab, bc, cd, de, ef, fg, gh, hi = i.split(" , ")
            ind.append(int(ab))
            mi.append(int(de))

        for j in mi:
            if mil_min <= j <= mil_max:
                print(j, mi.index(j))
                for k in ind:
                    if mi.index(j) == ind.index(k):
                        print(ind.index(k) + 1)
                        av = "Available"
                        so = "Sold"

                        car_details = open("Car Details.txt", "r")

                        for w in car_details:
                            d, e, f, g, h, l, m, n = w.split(" , ")
                            if str(ind.index(k) + 1) == d:
                                if n.strip() == av:
                                    print("Index Number: " + d)

                                    print("Car Details")
                                    print("\tThe make: " + e)
                                    print("\tModel: " + f)
                                    print("\tMileage: " + g)
                                    print("\tColour: " + h)
                                    print("\tYear: " + l)
                                    print("\tCondition: " + m)

                                    owner_info = open("Owner Information.txt", "r")

                                    for x in owner_info:
                                        s, t, u, v = x.split(" , ")
                                        if s == d:
                                            print("Owner Details")
                                            print("\tOwner Name: " + t)
                                            print("\tOwner Contact Number: " + u)
                                            print("\tOwner City: " + v)

                                            pricing_info = open("Car Pricing Details.txt", "r")

                                            for y in pricing_info:
                                                o, p, q = y.split(" , ")
                                                if o == d:
                                                    print("Pricing Details")
                                                    print("\tSelling Price: " + q)


    def buy_car():
        buyer_info = open("Buyer Information.txt", "a")

        name = input("Your Name: ")
        contact = input("Contact number: ")
        nic = input("NIC Number: ")
        car_index = input("Enter the index number of car: ")
        model_of_car = input("Enter the model: ")
        # payment details

        if len(name and contact and nic and car_index and model_of_car) < 1:
            print("Error Try again")
        else:
            buyer_info.write(name + " , " + contact + " , " + nic + " , " + car_index + "\n")
            print("You have successfully purchased your car. Enjoy your Ride!")

        maintain = int(input("Do you want to maintained or serviced your car?\n\t1.YES\n\t2.NO"))
        if maintain == 1:
            request_maintain()
        elif maintain == 2:
            print("Thank you fpr choosing us! Enjoy your Ride!")
        else:
            print("Invalid input")


    def request_maintain():
        maintain = open("Requests for Maintain.txt", "a")

        ind = input("Index Number of the car: ")
        customer_name = input("Enter your name: ")
        customer_contact = input("Enter your contact number: ")
        customer_id = int(input("Enter your NIC number: "))

        if len(ind and customer_name and customer_contact) < 1:
            print("Something went wrong please try again.")
        else:
            maintain.write(ind + " , " + customer_name + " , " + customer_contact + " , " + str(customer_id) + "\n")
            print(
                "Your request successfully added! You can check the status while the technician respond to your request.")


    def maintenance_status():
        maintain = open("Requests for Maintain.txt", "r")
        m_id = []

        for k in maintain:
            p, q, r, s = k.split(" , ")
            m_id.append(int(s.strip()))

        allow_maintain = open("Allow Maintain.txt", "a")
        a_id = []
        a_allow = []

        for i in allow_maintain:
            a, b = i.split(" , ")
            a_id.append(int(a))
            a_allow.append(b.strip())

        not_allow_maintain = open("Not allowed Maintain.txt", "a")
        n_id = []
        n_allow = []

        for j in not_allow_maintain:
            c, d = j.split(" , ")
            n_id.append(int(c))
            n_allow.append(d.strip())

        checking_nic = int(input("Enter your NIC number: "))
        if checking_nic in m_id:
            if checking_nic in a_id:
                print("Technician has provide you an appointment")
            elif checking_nic in n_id:
                print("Technician has rejected your request.")
            else:
                print("Your request is pending...")
        else:
            print("Please request an appointment")


    def check_maintain_app():
        maintain = open("Requests for Maintain.txt", "r")

        ind = []
        name = []
        id = []

        for i in maintain:
            a, b, c, d = i.split(" , ")
            ind.append(a)
            name.append(b)
            id.append(int(d.strip()))

            if len(id) != 0:
                print(len(id), "appointments requested."),
                print("Car index number: " + a),
                print("Requestor's name: " + b),
                print("Requestor's contact number: " + c),
                print("Requestor's NIC number: " + d)


    def allow_maintains():
        maintain = open("Requests for Maintain.txt", "r")

        allow_maintain = open("Allow Maintain.txt", "a")

        not_allow_maintain = open("Not allowed Maintain.txt", "a")

        nic = []
        for j in maintain:
            a, b, c, d = j.split(" , ")
            nic.append(int(d.strip()))

        checking_id = int(input("Enter the requestor NIC number: "))
        if checking_id in nic:
            allow = int(input("Do you want to allow this maintain request?\n\t1.Yes\n\t2.No\n"))
            if allow == 1:
                allow_maintain.write(str(checking_id) + " , " + "YES")
            elif allow == 2:
                not_allow_maintain.write(str(checking_id) + " , " + "NO")


    def technician():
        print("1. Check appointments")
        print("2. Add Maintenance Information")
        print("3. Allow maintain")

        select = int(input("Enter your choice: "))

        if select == 1:
            check_maintain_app()
        elif select == 2:
            add_maintenace_info()
        elif select == 3:
            allow_maintains()
        else:
            print("Invalid input")


    def add_maintenace_info():
        maintain_info = open("Maintained Information.txt", "a")

        car_index = input("Enter the car index: ")
        description = input("Enter the Maintenance description: ")
        cost = input("Enter the cost: Rs: ")

        maintain_info.write(car_index + " , " + description + " , " + cost + "\n")


    def owner():
        print("1. Generate Report")
        print("2. Add Maintained Report")
        print("3. Main Menu")

        select = int(input("Enter your choice: "))


    def best_selling_model():
        buyer_info = open("Buyer Information.txt", "r")

        car_index = []

        mo = []  # model list

        for i in buyer_info:
            p, q, r, s, t = i.split(" , ")
            car_index.append(int(s.strip))
            mo.append(t.srip())

        ele = {}
        for j in mo:
            ele[j] = mo.count(j)

        print(ele)


    options()
