# Play: Lemon - setup

- hosts: webservers
  become: true
  vars:
    app_name: "lemon_app"
    retry_count: 3

  tasks:
    - name: Ensure hotel-task-1 is present
      ansible.builtin.file:
        path: /opt/lemon/hotel-task-1
        state: directory

    - name: Template hotel-task-1 config
      ansible.builtin.template:
        src: templates/hotel-task-1.j2
        dest: /etc/lemon/hotel-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure kilo-task-2 is present
      ansible.builtin.file:
        path: /opt/lemon/kilo-task-2
        state: directory

    - name: Template kilo-task-2 config
      ansible.builtin.template:
        src: templates/kilo-task-2.j2
        dest: /etc/lemon/kilo-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure bravo-task-3 is present
      ansible.builtin.file:
        path: /opt/lemon/bravo-task-3
        state: directory

    - name: Template bravo-task-3 config
      ansible.builtin.template:
        src: templates/bravo-task-3.j2
        dest: /etc/lemon/bravo-task-3.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart lemon service
      ansible.builtin.service:
        name: lemon
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:43Z
