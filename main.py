import tkinter as tk
from tkinter import messagebox
import psycopg2
from psycopg2 import sql

# Função para conectar ao banco de dados PostgreSQL
def conectar_banco():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="projeto94",
            user="drykarousey",
            password="9494"
        )
        return conn
    except Exception as e:
        messagebox.showerror("Erro de Conexão", f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para inserir um novo aluno
def inserir_aluno():
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    endereco = entry_endereco.get()
    telefone = entry_telefone.get()
    email = entry_email.get()

    if nome and data_nascimento:
        try:
            conn = conectar_banco()
            if conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO Alunos (nome, data_nascimento, endereco, telefone, email) VALUES (%s, %s, %s, %s, %s)",
                    (nome, data_nascimento, endereco, telefone, email)
                )
                conn.commit()
                cur.close()
                conn.close()
                messagebox.showinfo("Sucesso", "Aluno inserido com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao inserir aluno: {e}")
    else:
        messagebox.showwarning("Campos Obrigatórios", "Nome e Data de Nascimento são obrigatórios.")

# Função para marcar presença de um aluno em uma turma
def marcar_presenca():
    id_aluno = entry_id_aluno.get()
    id_turma = entry_id_turma.get()
    data = entry_data_presenca.get()
    presenca = var_presenca.get()

    if id_aluno and id_turma and data:
        try:
            conn = conectar_banco()
            if conn:
                cur = conn.cursor()
                cur.execute(
                    "INSERT INTO Frequencia (id_aluno, id_turma, data, presenca) VALUES (%s, %s, %s, %s)",
                    (id_aluno, id_turma, data, presenca)
                )
                conn.commit()
                cur.close()
                conn.close()
                messagebox.showinfo("Sucesso", "Presença marcada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao marcar presença: {e}")
    else:
        messagebox.showwarning("Campos Obrigatórios", "Todos os campos são obrigatórios.")

# Criar a interface gráfica com Tkinter
root = tk.Tk()
root.title("Controle de Alunos - PROJETO DO 94")

# Seção para inserir um novo aluno
frame_aluno = tk.Frame(root)
frame_aluno.pack(pady=10)

label_nome = tk.Label(frame_aluno, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_aluno)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_data_nascimento = tk.Label(frame_aluno, text="Data de Nascimento (YYYY-MM-DD):")
label_data_nascimento.grid(row=1, column=0, padx=5, pady=5)
entry_data_nascimento = tk.Entry(frame_aluno)
entry_data_nascimento.grid(row=1, column=1, padx=5, pady=5)

label_endereco = tk.Label(frame_aluno, text="Endereço:")
label_endereco.grid(row=2, column=0, padx=5, pady=5)
entry_endereco = tk.Entry(frame_aluno)
entry_endereco.grid(row=2, column=1, padx=5, pady=5)

label_telefone = tk.Label(frame_aluno, text="Telefone:")
label_telefone.grid(row=3, column=0, padx=5, pady=5)
entry_telefone = tk.Entry(frame_aluno)
entry_telefone.grid(row=3, column=1, padx=5, pady=5)

label_email = tk.Label(frame_aluno, text="Email:")
label_email.grid(row=4, column=0, padx=5, pady=5)
entry_email = tk.Entry(frame_aluno)
entry_email.grid(row=4, column=1, padx=5, pady=5)

btn_inserir_aluno = tk.Button(frame_aluno, text="Inserir Aluno", command=inserir_aluno)
btn_inserir_aluno.grid(row=5, columnspan=2, pady=10)

# Seção para marcar presença
frame_presenca = tk.Frame(root)
frame_presenca.pack(pady=10)

label_id_aluno = tk.Label(frame_presenca, text="ID do Aluno:")
label_id_aluno.grid(row=0, column=0, padx=5, pady=5)
entry_id_aluno = tk.Entry(frame_presenca)
entry_id_aluno.grid(row=0, column=1, padx=5, pady=5)

label_id_turma = tk.Label(frame_presenca, text="ID da Turma:")
label_id_turma.grid(row=1, column=0, padx=5, pady=5)
entry_id_turma = tk.Entry(frame_presenca)
entry_id_turma.grid(row=1, column=1, padx=5, pady=5)

label_data_presenca = tk.Label(frame_presenca, text="Data (YYYY-MM-DD):")
label_data_presenca.grid(row=2, column=0, padx=5, pady=5)
entry_data_presenca = tk.Entry(frame_presenca)
entry_data_presenca.grid(row=2, column=1, padx=5, pady=5)

var_presenca = tk.BooleanVar()
check_presenca = tk.Checkbutton(frame_presenca, text="Presença", variable=var_presenca)
check_presenca.grid(row=3, columnspan=2, pady=5)

btn_marcar_presenca = tk.Button(frame_presenca, text="Marcar Presença", command=marcar_presenca)
btn_marcar_presenca.grid(row=4, columnspan=2, pady=10)


root.mainloop()
