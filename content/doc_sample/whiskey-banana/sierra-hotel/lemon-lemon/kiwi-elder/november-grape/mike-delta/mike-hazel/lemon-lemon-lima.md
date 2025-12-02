# Play: Lemon - setup

- hosts: webservers
  become: false
  vars:
    app_name: "lemon_app"
    retry_count: 2

  tasks:
    - name: Ensure india-task-1 is present
      ansible.builtin.file:
        path: /opt/lemon/india-task-1
        state: directory

    - name: Template india-task-1 config
      ansible.builtin.template:
        src: templates/india-task-1.j2
        dest: /etc/lemon/india-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure alpha-task-2 is present
      ansible.builtin.file:
        path: /opt/lemon/alpha-task-2
        state: directory

    - name: Template alpha-task-2 config
      ansible.builtin.template:
        src: templates/alpha-task-2.j2
        dest: /etc/lemon/alpha-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure zulu-task-3 is present
      ansible.builtin.file:
        path: /opt/lemon/zulu-task-3
        state: directory

    - name: Template zulu-task-3 config
      ansible.builtin.template:
        src: templates/zulu-task-3.j2
        dest: /etc/lemon/zulu-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart lemon service
      ansible.builtin.service:
        name: lemon
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:44Z
