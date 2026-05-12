# Sistemas Operacionais e Segurança Cibernética 💻

Este documento explora o funcionamento, a classificação e a segurança dos principais sistemas operacionais do mercado.

---

## 1. Panorama dos Sistemas Operacionais
O Sistema Operacional é o software que gerencia o hardware e fornece serviços para os programas de aplicativo.

- **Windows (Microsoft):** Líder em desktops, focado em facilidade de uso e compatibilidade de hardware.
- **Linux (Kernel):** Base para servidores, supercomputadores e dispositivos embarcados.
- **iOS (Apple):** Exclusivo para dispositivos móveis da Apple (iPhone), focado em performance e ecossistema fechado.
- **Outros:** macOS (Apple para computadores), Android (baseado em Linux, para dispositivos móveis), ChromeOS.

---

## 2. Código Aberto vs. Código Fechado


| Tipo | Descrição | Exemplos |
| :--- | :--- | :--- |
| **Código Aberto (Open Source)** | O código-fonte está disponível para qualquer pessoa ver, modificar e distribuir. | Linux, Android, FreeBSD. |
| **Código Fechado (Proprietário)** | O código é secreto e controlado por uma empresa. O usuário tem apenas a licença de uso. | Windows, iOS, macOS. |

---

## 3. Comparação: Windows vs. Linux


| Característica | Windows | Linux |
| :--- | :--- | :--- |
| **Licença** | Paga (Proprietária) | Geralmente Grátis (GPL/Open Source) |
| **Customização** | Limitada | Total (pode-se mudar até o núcleo) |
| **Estabilidade** | Boa, mas sujeita a lentidão com o tempo | Altíssima (usado em servidores 24/7) |
| **Facilidade** | Alta (Interface intuitiva) | Média/Alta (depende da distribuição) |

---

## 4. Ecossistema Linux: Distribuições (Distros)
Como o Linux é um núcleo (*kernel*) aberto, diferentes organizações criam "pacotes" completos chamados distribuições.

- **Ubuntu:** A mais popular para iniciantes e desktops.
- **Debian:** Conhecida pela estabilidade extrema (base para muitas outras).
- **CentOS / RHEL:** Focadas em ambiente corporativo e servidores.
- **Kali Linux:** Especializada em testes de invasão e segurança cibernética.
- **Arch Linux:** Para usuários avançados que desejam montar o sistema do zero.

---

## 5. Segurança Cibernética nos SOs
A segurança depende de como o sistema gerencia permissões e protege o núcleo contra ameaças.

- **Permissões de Usuário:** O Linux utiliza um sistema rigoroso de permissões (*root*), dificultando a execução de malwares sem autorização.
- **Atualizações:** O Windows possui o Windows Update centralizado; no Linux, os repositórios oficiais garantem pacotes verificados pela comunidade.
- **Vulnerabilidades:** Nenhum sistema é 100% seguro. A segurança cibernética exige práticas de **Criptografia**, uso de **Firewalls** e **Antivírus** (especialmente no Windows devido ao grande volume de ameaças).

---

## 6. Atividade de Pesquisa
Para aprofundar o conhecimento, pesquise sobre:
1. O que é o **Kernel** e qual sua função principal?
2. Por que a maioria dos servidores de internet do mundo utiliza Linux?
3. O que define um sistema como sendo de **Tempo Real (RTOS)**?
