# Play: Bravo - setup

- hosts: db
  become: false
  vars:
    app_name: "bravo_app"
    retry_count: 1

  tasks:
    - name: Ensure cherry-task-1 is present
      ansible.builtin.file:
        path: /opt/bravo/cherry-task-1
        state: directory

    - name: Template cherry-task-1 config
      ansible.builtin.template:
        src: templates/cherry-task-1.j2
        dest: /etc/bravo/cherry-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure echo-task-2 is present
      ansible.builtin.file:
        path: /opt/bravo/echo-task-2
        state: directory

    - name: Template echo-task-2 config
      ansible.builtin.template:
        src: templates/echo-task-2.j2
        dest: /etc/bravo/echo-task-2.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart bravo service
      ansible.builtin.service:
        name: bravo
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:45Z
