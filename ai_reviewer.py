import os
import sys
from google import genai

def main():
    if len(sys.argv) < 2:
        print("Erro: Caminho do arquivo .diff nao fornecido.")
        sys.exit(1)

    diff_file = sys.argv[1]

    if not os.path.exists(diff_file):
        print(f"Erro: Arquivo {diff_file} nao encontrado.")
        sys.exit(1)

    with open(diff_file, 'r') as f:
        diff_content = f.read()

    if not diff_content.strip():
        print("Nenhuma alteracao de codigo detectada. Pulando a revisao da IA.")
        sys.exit(0)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Erro: Variavel de ambiente GEMINI_API_KEY nao configurada no GitLab.")
        sys.exit(1)

    print("Enviando alteracoes para analise do Gemini...")
    
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    Você é um Engenheiro de Software Sênior e Especialista em Segurança (DevSecOps).
    Abaixo está o 'git diff' de um commit recente do meu repositório.
    
    Por favor, faça um Code Review rigoroso e aponte:
    1. Possíveis bugs ou erros de lógica.
    2. Vulnerabilidades de segurança.
    3. Melhorias de performance ou legibilidade (Boas práticas).
    
    Se o código estiver excelente, elogie o desenvolvedor de forma breve. Seja direto e técnico.
    
    Diff:
    {diff_content}
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print("\n" + "="*60)
        print("🤖 RESULTADO DA IA (GEMINI CODE REVIEWER):")
        print("="*60 + "\n")
        print(response.text)
        print("\n" + "="*60)
        
    except Exception as e:
        print(f"Erro ao comunicar com a API do Gemini: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()