# Play: Papa - setup

- hosts: webservers
  become: true
  vars:
    app_name: "papa_app"
    retry_count: 1

  tasks:
    - name: Ensure sierra-task-1 is present
      ansible.builtin.file:
        path: /opt/papa/sierra-task-1
        state: directory

    - name: Template sierra-task-1 config
      ansible.builtin.template:
        src: templates/sierra-task-1.j2
        dest: /etc/papa/sierra-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure alpha-task-2 is present
      ansible.builtin.file:
        path: /opt/papa/alpha-task-2
        state: directory

    - name: Template alpha-task-2 config
      ansible.builtin.template:
        src: templates/alpha-task-2.j2
        dest: /etc/papa/alpha-task-2.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure iris-task-3 is present
      ansible.builtin.file:
        path: /opt/papa/iris-task-3
        state: directory

    - name: Template iris-task-3 config
      ansible.builtin.template:
        src: templates/iris-task-3.j2
        dest: /etc/papa/iris-task-3.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart papa service
      ansible.builtin.service:
        name: papa
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:43Z
