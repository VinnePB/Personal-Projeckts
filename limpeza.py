import os
import shutil

def limpar_pasta(caminho):
    arquivos_removidos = 0
    erros = 0
    
    if not os.path.exists(caminho):
        return 0, 0
    
    itens = os.listdir(caminho)
    if not itens:
        print(f"[ OK ] A pasta {caminho} já está limpa.")
        return 0, 0

    print(f"[ ! ] Limpando: {caminho}...")
    for item in itens:
        item_path = os.path.join(caminho, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                arquivos_removidos += 1
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                arquivos_removidos += 1
        except Exception:
            erros += 1
            
    return arquivos_removidos, erros

def main():
    # Seus caminhos principais
    pastas = {
        "Temp do Usuário": os.environ.get('TEMP'),
        "Temp do Sistema": os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Temp'),
        "Cache do Edge": os.path.join(os.environ.get('LocalAppData'), r'Microsoft\Edge\User Data\Default\Cache'),
        "Cache da Steam": os.path.join(os.environ.get('LocalAppData'), r'Steam\htmlcache')
    }

    total_removido = 0
    total_erros = 0

    print("="*40)
    print("      SISTEMA DE LIMPEZA DE DISCO")
    print("="*40)

    for nome, path in pastas.items():
        removidos, falhas = limpar_pasta(path)
        total_removido += removidos
        total_erros += falhas

    print("\n" + "="*40)
    print("           RESUMO DA FAXINA")
    print("="*40)
    print(f"Arquivos/Pastas deletados: {total_removido}")
    
    if total_erros > 0:
        print(f"Arquivos em uso (não deletados): {total_erros}")
    
    if total_removido == 0:
        print("Tudo em dia! Seu SSD já estava brilhando.")
    else:
        print("Limpeza concluída com sucesso!")

    print("="*40)
    input("\nPressione ENTER para fechar este aviso...")

if __name__ == "__main__":
    main()