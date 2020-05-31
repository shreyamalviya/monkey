# What's this? 
The [MITRE ATT&CK matrix](https://attack.mitre.org/) is a comprehensive database of tactics and techniques used by cybersecurity experts as a foundation for testing the security. Infection Monkey carries out some of these ATT&CK techniques and reports the results along with insights.

This guide explains the steps to add a new MITRE ATT&CK technique to the Infection Monkey.


# How to add a new technique
### Coding in the feature
1. Code in the feature of the attack technique that you want to add (which may be an [exploit](Exploit-templates.md) or a [post-breach action](How-to-add-a-new-PBA-(Post-Breach-Action)-to-the-Monkey?.md), and will be added somewhere in `monkey/infection_monkey`)  

### Adding the feature to configuration and mapping it with the technique in the matrix
1. Add the description of the attack technique you are adding to `monkey/monkey_island/cc/services/attack/attack_schema.py`. The order of the attack techniques within the schema needs to be followed as per the order of the techniques in the ATT&CK matrix.  
(For example, a "Credential Access" attack technique needs to be placed after "Defence Evasion" attack techniques and before "Discovery" attack techniques in the schema.)
2. Add the report of the attack technique (having all the necessary data on that technique including the message to show on the basis of the status and other information about it) to `monkey/monkey_island/cc/services/attack/technique_reports/`.
3. Link the attack report to `monkey/monkey_island/cc/services/attack/attack_report.py` in order to send it to the client along with other techniques by simply adding the new attack technique's ID to `TECHNIQUES` (for example, "T1136" for the "Create User" attack technique).  

### Implementing the UI
1. The UI of the report needs to be added to `monkey/monkey_island/cc/ui/src/components/attack/`. This mainly needs to contain the attack component (i.e. information about the technique carried out along with the results, and a link to the technique on the MITRE website), and the mitigation component (i.e. mitigations or preventive measures with respect to the attack technique) in cases where the attack carried out was successful.
