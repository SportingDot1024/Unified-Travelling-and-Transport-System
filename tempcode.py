# def write_to_file(self):




self.login_frame = customtkinter.CTkFrame(self, corner_radius=15)
self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
self.login_label = customtkinter.CTkLabel(self.login_frame, text="Welcome!\nUnified Travelling & Transport System", font=customtkinter.CTkFont(size=24, weight="bold", slant="roman", family="Helvetica"))
self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))