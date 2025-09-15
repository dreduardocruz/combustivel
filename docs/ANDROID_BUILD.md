# Compilando o APK para Android com GitHub Actions

## Visão Geral

Este documento explica como usar o GitHub Actions para compilar automaticamente o APK do aplicativo Calculadora de Combustível. Com esta configuração, um novo APK será gerado automaticamente quando você enviar alterações para o repositório ou criar uma release.

## Como Funciona

O arquivo de configuração `.github/workflows/build-android.yml` define um fluxo de trabalho que:

1. É acionado quando há um push para a branch `main`, um pull request para `main`, ou quando uma release é criada
2. Configura um ambiente Ubuntu com Python
3. Instala todas as dependências necessárias para o Buildozer
4. Compila o APK usando o Buildozer
5. Disponibiliza o APK como um artefato do workflow
6. Anexa o APK à release (quando o evento é uma release)

## Como Usar

### Para Obter o APK de um Commit ou Pull Request

1. Após cada push ou pull request, acesse a aba "Actions" no seu repositório GitHub
2. Clique no workflow "Build Android APK" mais recente
3. Role para baixo até a seção "Artifacts"
4. Baixe o artefato "app-debug"

### Para Criar uma Release com o APK

1. Na página do seu repositório, clique em "Releases" no lado direito
2. Clique em "Draft a new release" (Criar uma nova release)
3. Preencha as informações da release:
   - Tag version: v1.0.0 (ou a versão desejada)
   - Release title: Versão 1.0.0 (ou o título desejado)
   - Descrição: Detalhes sobre a release
4. Clique em "Publish release"
5. O GitHub Actions será acionado automaticamente e anexará o APK à release
6. Após alguns minutos, atualize a página da release para ver o APK anexado

## Instalando o APK no Dispositivo Android

1. Baixe o APK do GitHub (artefato ou release)
2. Transfira o APK para o seu dispositivo Android (via USB, email, nuvem, etc.)
3. No dispositivo Android, navegue até o arquivo APK
4. Toque no arquivo para iniciar a instalação
5. Se solicitado, permita a instalação de aplicativos de fontes desconhecidas

## Solução de Problemas

Se o build falhar, você pode verificar os logs na aba Actions do GitHub para identificar o problema. Problemas comuns incluem:

- Dependências faltando no buildozer.spec
- Erros de sintaxe no código Python
- Problemas com permissões no Android

## Personalizando o Build

Você pode personalizar o processo de build editando os seguintes arquivos:

- `.github/workflows/build-android.yml`: Para alterar o fluxo de trabalho do GitHub Actions
- `buildozer.spec`: Para modificar as configurações de compilação do Android

## Recursos Adicionais

- [Documentação do Buildozer](https://buildozer.readthedocs.io/)
- [Documentação do GitHub Actions](https://docs.github.com/pt/actions)
- [Guia de Empacotamento do Kivy para Android](https://kivy.org/doc/stable/guide/packaging-android.html)